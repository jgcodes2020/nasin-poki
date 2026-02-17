#include <cstdlib>
#include <filesystem>
#include <format>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <string_view>

#include <libime/table/tablebaseddictionary.h>
#include <libime/table/tableoptions.h>
#include <simdjson.h>

void print_usage(int argc, char *argv[]) {
  std::cout << "usage: " << argv[0] << " [input] [output]" << std::endl;
}

int main(int argc, char *argv[]) {
  using namespace std::string_view_literals;
  using namespace simdjson;

  if (argc > 1 && argv[1] == "--help"sv) {
    print_usage(argc, argv);
    exit(0);
  } else if (argc != 3) {
    print_usage(argc, argv);
    exit(1);
  }

  auto input_json = padded_string::load(argv[1]);
  auto output_dict = libime::TableBasedDictionary{};

  ondemand::parser parser;
  auto table = parser.iterate(input_json);

  auto key_code = table["key_code"].get_string().value();
  auto length = table["length"].get_int64().value();

  {
    std::string config_init =
        std::format("KeyCode={}\nLength={}\n[Data]\n", key_code, length);
    std::istringstream iss{config_init};
    output_dict.load(iss, libime::TableFormat::Text);
  }

  for (auto field : table["data"].get_object()) {
    auto key = field.escaped_key().value();
    auto value = field.value()->get_string().value();
    std::cout << "\"" << key << "\" -> \"" << value << "\"\n";
    output_dict.insert(key, value);
  }
  std::cout << std::flush;

  {
    std::ofstream file(argv[2], std::ios::binary);
    output_dict.save(file, libime::TableFormat::Binary);
    // output_dict.isInputCode(uint32_t c)
  }
}
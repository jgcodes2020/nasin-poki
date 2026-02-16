cmake_minimum_required(VERSION 3.24)
project(fcitx5-nasin-poki
    VERSION 0.1.0
)

find_package(LibIMETable REQUIRED)
find_package(Fcitx5Utils REQUIRED)
find_package(Fcitx5Core REQUIRED)

# Setup some compiler option that is generally useful and compatible with Fcitx 5 (C++17)
include("${FCITX_INSTALL_CMAKECONFIG_DIR}/Fcitx5Utils/Fcitx5CompilerSettings.cmake")

# Addon file (declares the table/registration file)
install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/nasin-poki-addon.conf" RENAME nasin-poki.conf DESTINATION "${FCITX_INSTALL_PKGDATADIR}/addon")

# Make the dictionary
set(mb_file "${CMAKE_CURRENT_BINARY_DIR}/nasin-poki.main.dict")
add_custom_command(OUTPUT "nasin-poki.main.dict"
  DEPENDS "nasin-poki.txt"
  COMMAND LibIME::tabledict ARGS "${CMAKE_CURRENT_SOURCE_DIR}/nasin-poki.txt"
  "${CMAKE_CURRENT_BINARY_DIR}/nasin-poki.main.dict")
add_custom_target(table_data ALL DEPENDS "${mb_file}")

# Input Method registration file
install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/nasin-poki.conf" DESTINATION "${FCITX_INSTALL_PKGDATADIR}/inputmethod")
# Table dictionary
install(FILES "${mb_file}" DESTINATION "${FCITX_INSTALL_PKGDATADIR}/table")
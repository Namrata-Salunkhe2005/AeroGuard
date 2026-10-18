# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_f450_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED f450_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(f450_FOUND FALSE)
  elseif(NOT f450_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(f450_FOUND FALSE)
  endif()
  return()
endif()
set(_f450_CONFIG_INCLUDED TRUE)

# output package information
if(NOT f450_FIND_QUIETLY)
  message(STATUS "Found f450: 0.0.1 (${f450_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'f450' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${f450_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(f450_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${f450_DIR}/${_extra}")
endforeach()

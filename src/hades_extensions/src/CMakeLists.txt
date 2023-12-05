# Fetch the pybind11 repository and initialise it
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

# Create the C++ library which will be used for the tests and the Python module
add_library(${CPP_LIB} STATIC
        ${CMAKE_SOURCE_DIR}/src/game_objects/registry.cpp
        ${CMAKE_SOURCE_DIR}/src/game_objects/steering.cpp
        ${CMAKE_SOURCE_DIR}/src/game_objects/systems/armour_regen.cpp
        ${CMAKE_SOURCE_DIR}/src/game_objects/systems/attacks.cpp
        ${CMAKE_SOURCE_DIR}/src/game_objects/systems/effects.cpp
        ${CMAKE_SOURCE_DIR}/src/game_objects/systems/inventory.cpp
        ${CMAKE_SOURCE_DIR}/src/game_objects/systems/movements.cpp
        ${CMAKE_SOURCE_DIR}/src/game_objects/systems/upgrade.cpp
        ${CMAKE_SOURCE_DIR}/src/generation/astar.cpp
        ${CMAKE_SOURCE_DIR}/src/generation/bsp.cpp
        ${CMAKE_SOURCE_DIR}/src/generation/map.cpp
        ${CMAKE_SOURCE_DIR}/src/generation/primitives.cpp
)
target_include_directories(${CPP_LIB} PUBLIC ${CMAKE_SOURCE_DIR}/include)

# Create the Python module
pybind11_add_module(${PY_MODULE} ${CMAKE_SOURCE_DIR}/src/binding.cpp)
target_compile_definitions(${PY_MODULE} PRIVATE Py_DEBUG)
target_link_libraries(${PY_MODULE} PRIVATE ${CPP_LIB})

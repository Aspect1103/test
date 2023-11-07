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
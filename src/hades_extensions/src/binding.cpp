// Std headers
#include <optional>

// External headers
#include <pybind11/functional.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

// Local headers
#include "game_objects/stats.hpp"
#include "game_objects/steering.hpp"
#include "game_objects/systems/armour_regen.hpp"
#include "game_objects/systems/attacks.hpp"
#include "game_objects/systems/effects.hpp"
#include "game_objects/systems/inventory.hpp"
#include "game_objects/systems/movements.hpp"
#include "game_objects/systems/upgrade.hpp"
#include "generation/map.hpp"

// ----- STRUCTURES ------------------------------------------


// ----- PYTHON MODULE CREATION ------------------------------
PYBIND11_MODULE(hades_extensions, module) {  // NOLINT
  // Add the module docstring and the custom converters
  module.doc() = "Manages the various C++ extension modules for the game.";
}

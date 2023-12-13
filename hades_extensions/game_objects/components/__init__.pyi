# Custom
from hades_extensions.game_objects import (
    ActionFunction,
    AttackAlgorithm,
    ComponentBase,
    StatusEffectType,
    SteeringBehaviours,
    SteeringMovementState,
    Vec2d,
)

class Stat(ComponentBase):
    def __init__(self: Stat, value: float, maximum_level: float) -> None: ...
    def get_value(self: Stat) -> float: ...
    def set_value(self: Stat, new_value: float) -> None: ...
    def get_max_value(self: Stat) -> float: ...
    def add_to_max_value(self: Stat, value: float) -> None: ...
    def get_current_level(self: Stat) -> float: ...
    def increment_current_level(self: Stat) -> None: ...
    def get_max_level(self: Stat) -> float: ...

class Armour(Stat): ...
class ArmourRegen(Stat): ...

class Attacks(ComponentBase):
    attack_algorithms: list[AttackAlgorithm]
    attack_state: int
    def __init__(self: Attacks, attack_algorithms: list[AttackAlgorithm]) -> None: ...

# TODO: decide where this should go
class StatusEffectData:
    status_effect_type: StatusEffectType
    increase: ActionFunction
    def __init__(
        self: StatusEffectData,
        status_effect_type: StatusEffectType,
        increase: ActionFunction,
        duration: ActionFunction,
        interval: ActionFunction,
    ) -> None: ...

class EffectApplier(ComponentBase):
    def __init__(
        self: EffectApplier,
        instant_effects: dict[type[ComponentBase], ActionFunction],
        status_effects: dict[type[ComponentBase], StatusEffectData],
    ) -> None: ...

class Footprints(ComponentBase):
    footprints: list[int]
    def __init__(self: Footprints) -> None: ...

class Health(Stat): ...

class Inventory(ComponentBase):
    width: int
    height: int
    items: list[int]
    def __init__(self: Inventory, width: int, height: int) -> None: ...
    def get_capacity(self: Inventory) -> int: ...

class KeyboardMovement(ComponentBase):
    moving_north: bool
    moving_east: bool
    moving_south: bool
    moving_west: bool
    def __init__(self: KeyboardMovement) -> None: ...

class Money(ComponentBase):
    money: int
    def __init__(self: Money, money: int) -> None: ...

class MovementForce(Stat): ...

class StatusEffect:
    value: float
    duration: float
    interval: float
    target_component: type[ComponentBase]

class StatusEffects(ComponentBase):
    def __init__(self: StatusEffects) -> None: ...

class SteeringMovement(ComponentBase):
    behaviours: dict[SteeringMovementState, list[SteeringBehaviours]]
    movement_state: SteeringMovementState
    target_id: int
    path_list: list[Vec2d]
    def __init__(
        self: SteeringMovement,
        behaviours: dict[SteeringMovementState, list[SteeringBehaviours]],
    ) -> None: ...

class Upgrades(ComponentBase):
    def __init__(
        self: Upgrades,
        upgrades: dict[type[ComponentBase], ActionFunction],
    ) -> None: ...

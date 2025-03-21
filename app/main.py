from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0]
        super().__init__(weight=weight)
        self.name, self.coords = name, coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name=name, weight=weight, coords=coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        current_load: None | Cargo,
        coords: list | None = None,
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight, self.current_load = max_load_weight, current_load

    def hook_load(self, robot: Cargo) -> None:
        if not self.current_load and robot.weight <= self.max_load_weight:
            self.current_load = robot

    def unhook_load(self) -> None:
        self.current_load = None

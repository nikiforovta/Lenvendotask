from dataclasses import dataclass, field


@dataclass(order=True)
class JsTestTask:
    name: str = ''
    image: str = ''
    price: int = 0
    sort_index: str = field(init=False, repr=False)

    def __post_init__(self):
        self.sort_index = self.name

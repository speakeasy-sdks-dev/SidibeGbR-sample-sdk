"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import drinktype as shared_drinktype
from dataclasses_json import Undefined, dataclass_json
from speakeasybar import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DrinkInput:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the drink."""
    price: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('price') }})
    r"""The price of one unit of the drink in US cents."""
    product_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productCode'), 'exclude': lambda f: f is None }})
    r"""The product code of the drink, only available when authenticated."""
    type: Optional[shared_drinktype.DrinkType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The type of drink."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Drink:
    r"""A drink."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the drink."""
    price: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('price') }})
    r"""The price of one unit of the drink in US cents."""
    product_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productCode'), 'exclude': lambda f: f is None }})
    r"""The product code of the drink, only available when authenticated."""
    stock: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stock'), 'exclude': lambda f: f is None }})
    r"""The number of units of the drink in stock, only available when authenticated."""
    type: Optional[shared_drinktype.DrinkType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The type of drink."""
    


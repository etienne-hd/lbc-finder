from lbc import Category, Region, Department, City, OwnerType

from typing import overload


class Parameters:
    @overload
    def __init__(
        self,
        url: str | None = None,
        text: str | None = None,
        category: Category = Category.TOUTES_CATEGORIES,
        locations: list[Region | Department | City]
        | Region
        | Department
        | City
        | None = None,
        limit: int = 35,
        limit_alu: int = 3,
        page: int = 1,
        owner_type: OwnerType | None = None,
        shippable: bool | None = None,
        search_in_title_only: bool = False,
        **kwargs,
    ): ...

    def __init__(self, **kwargs):
        self._kwargs = kwargs

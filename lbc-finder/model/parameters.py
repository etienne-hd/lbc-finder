from typing import Optional, Union, List
from lbc import Category, Region, Department, City, OwnerType

from typing import overload

class Parameters:
    @overload
    def __init__(
        self,
        url: Optional[str] = None,
        text: Optional[str] = None,
        category: Category = Category.TOUTES_CATEGORIES,
        locations: Optional[Union[List[Union[Region, Department, City]], Union[Region, Department, City]]] = None,
        limit: int = 35,
        limit_alu: int = 3,
        page: int = 1,
        owner_type: Optional[OwnerType] = None,
        shippable: Optional[bool] = None,
        search_in_title_only: bool = False,
        **kwargs
    ): ...
    
    def __init__(self, **kwargs):
        self._kwargs = kwargs
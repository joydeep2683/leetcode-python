from typing import *


def containsDuplicateV1(nums: List[int]) -> bool:
    store = set()
    for num in nums:
        if num in store:
            return True
        store.add(num)
    return False
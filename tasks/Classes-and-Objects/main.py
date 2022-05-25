from typing import List, TypeVar

# bounded self type
Self = TypeVar("Self", bound="Student")


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self: Self, name: str, age: int, tracks: List[str], score: float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def __str__(self: Self):
        return f"Student({name}): score: {self.score}"

    def change_name(self: Self, new_name: str):
        self.name = new_name

    def change_age(self: Self, new_age: int):
        self.age = new_age

    def add_track(self: Self, new_track: str):
        self.tracks.append(new_track)

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
score = Bob.get_score()

print(score)

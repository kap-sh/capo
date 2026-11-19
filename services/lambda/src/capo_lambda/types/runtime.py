"""Generated from Smithy shape ``com.amazonaws.lambda#Runtime``."""

from typing import Literal, TypeAlias, cast

Runtime: TypeAlias = Literal[
    "nodejs",
    "nodejs4.3",
    "nodejs6.10",
    "nodejs8.10",
    "nodejs10.x",
    "nodejs12.x",
    "nodejs14.x",
    "nodejs16.x",
    "nodejs18.x",
    "nodejs20.x",
    "nodejs22.x",
    "nodejs24.x",
    "java8",
    "java8.al2",
    "java11",
    "java17",
    "java21",
    "java25",
    "python2.7",
    "python3.6",
    "python3.7",
    "python3.8",
    "python3.9",
    "python3.10",
    "python3.11",
    "python3.12",
    "python3.13",
    "python3.14",
    "dotnetcore1.0",
    "dotnetcore2.0",
    "dotnetcore2.1",
    "dotnetcore3.1",
    "dotnet6",
    "dotnet8",
    "dotnet10",
    "nodejs4.3-edge",
    "go1.x",
    "ruby2.5",
    "ruby2.7",
    "ruby3.2",
    "ruby3.3",
    "ruby3.4",
    "ruby4.0",
    "provided",
    "provided.al2",
    "provided.al2023",
    "nodejs26.x",
    "python3.15",
    "java8.al2023",
    "java11.al2023",
    "java17.al2023",
    "custom",
]


# --- restJson1 ser/de ---
def serialize_json(value: Runtime) -> str:
    return value


def deserialize_json(data: str) -> Runtime:
    return cast(Runtime, data)

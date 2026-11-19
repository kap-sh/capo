"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerEnvironment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_zero_and255_max_string


class ContainerEnvironment(TypedDict, closed=True):
    name: NotRequired[
        "capo_gamelift.types.non_zero_and255_max_string.NonZeroAnd255MaxString"
    ]
    """<p>The environment variable name.</p>"""
    value: NotRequired[
        "capo_gamelift.types.non_zero_and255_max_string.NonZeroAnd255MaxString"
    ]
    """<p>The environment variable value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerEnvironment) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerEnvironment:
    out: ContainerEnvironment = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerEnvironment) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> ContainerEnvironment:
    out: ContainerEnvironment = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out

"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeBuildOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.build


class DescribeBuildOutput(TypedDict, closed=True):
    build: NotRequired["capo_gamelift.types.build.Build"]
    """<p>Set of properties describing the requested build.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBuildOutput) -> dict:
    out: dict = {}
    if "build" in value:
        import capo_gamelift.types.build

        out["Build"] = capo_gamelift.types.build.serialize_aws_json_1_1(value["build"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBuildOutput:
    out: DescribeBuildOutput = {}  # type: ignore[typeddict-item]
    if data.get("Build") is not None:
        import capo_gamelift.types.build

        out["build"] = capo_gamelift.types.build.deserialize_aws_json_1_1(data["Build"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeBuildOutput) -> dict:
    out: dict = {}
    if "build" in value:
        import capo_gamelift.types.build

        out["Build"] = capo_gamelift.types.build.serialize_cbor(value["build"])
    return out


def deserialize_cbor(data: dict) -> DescribeBuildOutput:
    out: DescribeBuildOutput = {}  # type: ignore[typeddict-item]
    if data.get("Build") is not None:
        import capo_gamelift.types.build

        out["build"] = capo_gamelift.types.build.deserialize_cbor(data["Build"])
    return out

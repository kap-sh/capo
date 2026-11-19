"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.stage_name


class StageContext(TypedDict, closed=True):
    name: NotRequired["capo_codepipeline.types.stage_name.StageName"]
    """<p>The name of the stage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageContext) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StageContext:
    out: StageContext = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StageContext) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> StageContext:
    out: StageContext = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out

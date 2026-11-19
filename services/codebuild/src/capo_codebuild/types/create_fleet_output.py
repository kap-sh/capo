"""Generated from Smithy shape ``com.amazonaws.codebuild#CreateFleetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.fleet


class CreateFleetOutput(TypedDict, closed=True):
    fleet: NotRequired["capo_codebuild.types.fleet.Fleet"]
    """<p>Information about the compute fleet</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFleetOutput) -> dict:
    out: dict = {}
    if "fleet" in value:
        import capo_codebuild.types.fleet

        out["fleet"] = capo_codebuild.types.fleet.serialize_aws_json_1_1(value["fleet"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFleetOutput:
    out: CreateFleetOutput = {}  # type: ignore[typeddict-item]
    if data.get("fleet") is not None:
        import capo_codebuild.types.fleet

        out["fleet"] = capo_codebuild.types.fleet.deserialize_aws_json_1_1(
            data["fleet"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateFleetOutput) -> dict:
    out: dict = {}
    if "fleet" in value:
        import capo_codebuild.types.fleet

        out["fleet"] = capo_codebuild.types.fleet.serialize_cbor(value["fleet"])
    return out


def deserialize_cbor(data: dict) -> CreateFleetOutput:
    out: CreateFleetOutput = {}  # type: ignore[typeddict-item]
    if data.get("fleet") is not None:
        import capo_codebuild.types.fleet

        out["fleet"] = capo_codebuild.types.fleet.deserialize_cbor(data["fleet"])
    return out

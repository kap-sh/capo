"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetFleetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.fleet_names
    import capo_codebuild.types.fleets


class BatchGetFleetsOutput(TypedDict, closed=True):
    fleets: NotRequired["capo_codebuild.types.fleets.Fleets"]
    """<p>Information about the requested compute fleets.</p>"""
    fleets_not_found: NotRequired["capo_codebuild.types.fleet_names.FleetNames"]
    """<p>The names of compute fleets for which information could not be found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetFleetsOutput) -> dict:
    out: dict = {}
    if "fleets" in value:
        import capo_codebuild.types.fleets

        out["fleets"] = capo_codebuild.types.fleets.serialize_aws_json_1_1(
            value["fleets"]
        )
    if "fleets_not_found" in value:
        import capo_codebuild.types.fleet_names

        out["fleetsNotFound"] = capo_codebuild.types.fleet_names.serialize_aws_json_1_1(
            value["fleets_not_found"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetFleetsOutput:
    out: BatchGetFleetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("fleets") is not None:
        import capo_codebuild.types.fleets

        out["fleets"] = capo_codebuild.types.fleets.deserialize_aws_json_1_1(
            data["fleets"]
        )
    if data.get("fleetsNotFound") is not None:
        import capo_codebuild.types.fleet_names

        out["fleets_not_found"] = (
            capo_codebuild.types.fleet_names.deserialize_aws_json_1_1(
                data["fleetsNotFound"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetFleetsOutput) -> dict:
    out: dict = {}
    if "fleets" in value:
        import capo_codebuild.types.fleets

        out["fleets"] = capo_codebuild.types.fleets.serialize_cbor(value["fleets"])
    if "fleets_not_found" in value:
        import capo_codebuild.types.fleet_names

        out["fleetsNotFound"] = capo_codebuild.types.fleet_names.serialize_cbor(
            value["fleets_not_found"]
        )
    return out


def deserialize_cbor(data: dict) -> BatchGetFleetsOutput:
    out: BatchGetFleetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("fleets") is not None:
        import capo_codebuild.types.fleets

        out["fleets"] = capo_codebuild.types.fleets.deserialize_cbor(data["fleets"])
    if data.get("fleetsNotFound") is not None:
        import capo_codebuild.types.fleet_names

        out["fleets_not_found"] = capo_codebuild.types.fleet_names.deserialize_cbor(
            data["fleetsNotFound"]
        )
    return out

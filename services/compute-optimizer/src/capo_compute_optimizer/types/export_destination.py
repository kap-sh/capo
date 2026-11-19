"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.s3_destination


class ExportDestination(TypedDict, closed=True):
    s3: NotRequired["capo_compute_optimizer.types.s3_destination.S3Destination"]
    """<p>An object that describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and object keys of a recommendations export file, and its associated metadata file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportDestination) -> dict:
    out: dict = {}
    if "s3" in value:
        import capo_compute_optimizer.types.s3_destination

        out["s3"] = capo_compute_optimizer.types.s3_destination.serialize_aws_json_1_0(
            value["s3"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportDestination:
    out: ExportDestination = {}  # type: ignore[typeddict-item]
    if data.get("s3") is not None:
        import capo_compute_optimizer.types.s3_destination

        out["s3"] = (
            capo_compute_optimizer.types.s3_destination.deserialize_aws_json_1_0(
                data["s3"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportDestination) -> dict:
    out: dict = {}
    if "s3" in value:
        import capo_compute_optimizer.types.s3_destination

        out["s3"] = capo_compute_optimizer.types.s3_destination.serialize_cbor(
            value["s3"]
        )
    return out


def deserialize_cbor(data: dict) -> ExportDestination:
    out: ExportDestination = {}  # type: ignore[typeddict-item]
    if data.get("s3") is not None:
        import capo_compute_optimizer.types.s3_destination

        out["s3"] = capo_compute_optimizer.types.s3_destination.deserialize_cbor(
            data["s3"]
        )
    return out

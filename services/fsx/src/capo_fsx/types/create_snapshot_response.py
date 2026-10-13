"""Generated from Smithy shape ``com.amazonaws.fsx#CreateSnapshotResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.snapshot


class CreateSnapshotResponse(TypedDict, closed=True):
    snapshot: NotRequired["capo_fsx.types.snapshot.Snapshot"]
    """<p>A description of the snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotResponse) -> dict:
    out: dict = {}
    if "snapshot" in value:
        import capo_fsx.types.snapshot

        out["Snapshot"] = capo_fsx.types.snapshot.serialize_aws_json_1_1(
            value["snapshot"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotResponse:
    out: CreateSnapshotResponse = {}  # type: ignore[typeddict-item]
    if data.get("Snapshot") is not None:
        import capo_fsx.types.snapshot

        out["snapshot"] = capo_fsx.types.snapshot.deserialize_aws_json_1_1(
            data["Snapshot"]
        )
    return out


def redact_sensitive(value: CreateSnapshotResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "snapshot" in value:
        import capo_fsx.types.snapshot

        out["snapshot"] = capo_fsx.types.snapshot.redact_sensitive(value["snapshot"])
    return out

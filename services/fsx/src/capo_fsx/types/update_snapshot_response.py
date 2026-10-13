"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateSnapshotResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.snapshot


class UpdateSnapshotResponse(TypedDict, closed=True):
    snapshot: NotRequired["capo_fsx.types.snapshot.Snapshot"]
    """<p>Returned after a successful <code>UpdateSnapshot</code> operation, describing the snapshot that you updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSnapshotResponse) -> dict:
    out: dict = {}
    if "snapshot" in value:
        import capo_fsx.types.snapshot

        out["Snapshot"] = capo_fsx.types.snapshot.serialize_aws_json_1_1(
            value["snapshot"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSnapshotResponse:
    out: UpdateSnapshotResponse = {}  # type: ignore[typeddict-item]
    if data.get("Snapshot") is not None:
        import capo_fsx.types.snapshot

        out["snapshot"] = capo_fsx.types.snapshot.deserialize_aws_json_1_1(
            data["Snapshot"]
        )
    return out


def redact_sensitive(value: UpdateSnapshotResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "snapshot" in value:
        import capo_fsx.types.snapshot

        out["snapshot"] = capo_fsx.types.snapshot.redact_sensitive(value["snapshot"])
    return out

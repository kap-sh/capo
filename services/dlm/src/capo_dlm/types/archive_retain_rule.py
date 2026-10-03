"""Generated from Smithy shape ``com.amazonaws.dlm#ArchiveRetainRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.retention_archive_tier


class ArchiveRetainRule(TypedDict, closed=True):
    retention_archive_tier: NotRequired[
        "capo_dlm.types.retention_archive_tier.RetentionArchiveTier"
    ]
    """<p>Information about retention period in the Amazon EBS Snapshots Archive. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/snapshot-archive.html">Archive Amazon EBS snapshots</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveRetainRule) -> dict:
    out: dict = {}
    if "retention_archive_tier" in value:
        import capo_dlm.types.retention_archive_tier

        out["RetentionArchiveTier"] = (
            capo_dlm.types.retention_archive_tier.serialize_json(
                value["retention_archive_tier"]
            )
        )
    return out


def deserialize_json(data: dict) -> ArchiveRetainRule:
    out: ArchiveRetainRule = {}  # type: ignore[typeddict-item]
    if data.get("RetentionArchiveTier") is not None:
        import capo_dlm.types.retention_archive_tier

        out["retention_archive_tier"] = (
            capo_dlm.types.retention_archive_tier.deserialize_json(
                data["RetentionArchiveTier"]
            )
        )
    return out

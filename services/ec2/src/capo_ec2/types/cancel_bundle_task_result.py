"""Generated from Smithy shape ``com.amazonaws.ec2#CancelBundleTaskResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.bundle_task


class CancelBundleTaskResult(TypedDict, closed=True):
    bundle_task: NotRequired["capo_ec2.types.bundle_task.BundleTask"]
    """<p>Information about the bundle task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelBundleTaskResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "bundle_task" in value:
        import capo_ec2.types.bundle_task

        capo_ec2.types.bundle_task.serialize_ec2_query(
            value["bundle_task"], pairs, f"{key_prefix}BundleInstanceTask"
        )


def deserialize_ec2_query(el: Element) -> CancelBundleTaskResult:
    out: CancelBundleTaskResult = {}  # type: ignore[typeddict-item]
    child_bundle_task = el.find("bundleInstanceTask")
    if child_bundle_task is not None:
        import capo_ec2.types.bundle_task

        out["bundle_task"] = capo_ec2.types.bundle_task.deserialize_ec2_query(
            child_bundle_task
        )
    return out


def redact_sensitive(value: CancelBundleTaskResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bundle_task" in value:
        import capo_ec2.types.bundle_task

        out["bundle_task"] = capo_ec2.types.bundle_task.redact_sensitive(
            value["bundle_task"]
        )
    return out

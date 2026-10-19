"""Generated from Smithy shape ``com.amazonaws.backup#CreateFrameworkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.framework_controls
    import capo_backup.types.framework_description
    import capo_backup.types.framework_name
    import capo_backup.types.string
    import capo_backup.types.string_map


class CreateFrameworkInput(TypedDict, closed=True):
    framework_name: "capo_backup.types.framework_name.FrameworkName"
    """<p>The unique name of the framework. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>"""
    framework_description: NotRequired[
        "capo_backup.types.framework_description.FrameworkDescription"
    ]
    """<p>An optional description of the framework with a maximum of 1,024 characters.</p>"""
    framework_controls: "capo_backup.types.framework_controls.FrameworkControls"
    """<p>The controls that make up the framework. Each control in the list has a name, input parameters, and scope.</p>"""
    idempotency_token: NotRequired["capo_backup.types.string.string"]
    """<p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>CreateFrameworkInput</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""
    framework_tags: NotRequired["capo_backup.types.string_map.stringMap"]
    """<p>The tags to assign to the framework.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFrameworkInput) -> dict:
    out: dict = {}
    out["FrameworkName"] = value["framework_name"]
    if "framework_description" in value:
        out["FrameworkDescription"] = value["framework_description"]
    import capo_backup.types.framework_controls

    out["FrameworkControls"] = capo_backup.types.framework_controls.serialize_json(
        value["framework_controls"]
    )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    if "framework_tags" in value:
        import capo_backup.types.string_map

        out["FrameworkTags"] = capo_backup.types.string_map.serialize_json(
            value["framework_tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateFrameworkInput:
    out: CreateFrameworkInput = {}  # type: ignore[typeddict-item]
    if data.get("FrameworkName") is not None:
        out["framework_name"] = data["FrameworkName"]
    else:
        out["framework_name"] = ""
    if data.get("FrameworkDescription") is not None:
        out["framework_description"] = data["FrameworkDescription"]
    if data.get("FrameworkControls") is not None:
        import capo_backup.types.framework_controls

        out["framework_controls"] = (
            capo_backup.types.framework_controls.deserialize_json(
                data["FrameworkControls"]
            )
        )
    else:
        out["framework_controls"] = []
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("FrameworkTags") is not None:
        import capo_backup.types.string_map

        out["framework_tags"] = capo_backup.types.string_map.deserialize_json(
            data["FrameworkTags"]
        )
    return out

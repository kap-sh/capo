"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomActionURLOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.url_operation_template
    import capo_quicksight.types.url_target_configuration


class CustomActionURLOperation(TypedDict, closed=True):
    url_template: "capo_quicksight.types.url_operation_template.URLOperationTemplate"
    """<p>THe URL link of the <code>CustomActionURLOperation</code>.</p>"""
    url_target: "capo_quicksight.types.url_target_configuration.URLTargetConfiguration"
    """<p>The target of the <code>CustomActionURLOperation</code>.</p> <p>Valid values are defined as follows:</p> <ul> <li> <p> <code>NEW_TAB</code>: Opens the target URL in a new browser tab.</p> </li> <li> <p> <code>NEW_WINDOW</code>: Opens the target URL in a new browser window.</p> </li> <li> <p> <code>SAME_TAB</code>: Opens the target URL in the same browser tab.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionURLOperation) -> dict:
    out: dict = {}
    out["URLTemplate"] = value["url_template"]
    import capo_quicksight.types.url_target_configuration

    out["URLTarget"] = capo_quicksight.types.url_target_configuration.serialize_json(
        value["url_target"]
    )
    return out


def deserialize_json(data: dict) -> CustomActionURLOperation:
    out: CustomActionURLOperation = {}  # type: ignore[typeddict-item]
    if data.get("URLTemplate") is not None:
        out["url_template"] = data["URLTemplate"]
    else:
        out["url_template"] = ""
    if data.get("URLTarget") is not None:
        import capo_quicksight.types.url_target_configuration

        out["url_target"] = (
            capo_quicksight.types.url_target_configuration.deserialize_json(
                data["URLTarget"]
            )
        )
    else:
        import typing

        out["url_target"] = typing.cast(
            "capo_quicksight.types.url_target_configuration.URLTargetConfiguration", ""
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.iot#ReplaceDefaultPolicyVersionParams``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.policy_template_name


class ReplaceDefaultPolicyVersionParams(TypedDict, closed=True):
    template_name: "capo_iot.types.policy_template_name.PolicyTemplateName"
    """<p>The name of the template to be applied. The only supported value is <code>BLANK_POLICY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplaceDefaultPolicyVersionParams) -> dict:
    out: dict = {}
    import capo_iot.types.policy_template_name

    out["templateName"] = capo_iot.types.policy_template_name.serialize_json(
        value["template_name"]
    )
    return out


def deserialize_json(data: dict) -> ReplaceDefaultPolicyVersionParams:
    out: ReplaceDefaultPolicyVersionParams = {}  # type: ignore[typeddict-item]
    if data.get("templateName") is not None:
        import capo_iot.types.policy_template_name

        out["template_name"] = capo_iot.types.policy_template_name.deserialize_json(
            data["templateName"]
        )
    else:
        import typing

        out["template_name"] = typing.cast(
            "capo_iot.types.policy_template_name.PolicyTemplateName", ""
        )
    return out

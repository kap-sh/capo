"""Generated from Smithy shape ``com.amazonaws.elementalinference#TemplateGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.template_uri_list


class TemplateGroup(TypedDict, closed=True):
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>A name for the template group.</p>"""
    template_uris: "capo_elementalinference.types.template_uri_list.TemplateUriList"
    """<p>An array of Amazon S3 URIs that point to the graphics-compositing templates for this group. You can specify 1 or 2 URIs. Each URI must be in the form <code>s3://bucket-name/key</code>. Elemental Inference reads these templates using the IAM role that you specify in accessRoleArn. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateGroup) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_elementalinference.types.template_uri_list

    out["templateUris"] = (
        capo_elementalinference.types.template_uri_list.serialize_json(
            value["template_uris"]
        )
    )
    return out


def deserialize_json(data: dict) -> TemplateGroup:
    out: TemplateGroup = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("templateUris") is not None:
        import capo_elementalinference.types.template_uri_list

        out["template_uris"] = (
            capo_elementalinference.types.template_uri_list.deserialize_json(
                data["templateUris"]
            )
        )
    else:
        out["template_uris"] = []
    return out

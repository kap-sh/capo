"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateInAppTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.in_app_template_request


class UpdateInAppTemplateRequest(TypedDict, closed=True):
    create_new_version: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>"""
    in_app_template_request: NotRequired[
        "capo_pinpoint.types.in_app_template_request.InAppTemplateRequest"
    ]
    template_name: "capo_pinpoint.types.__string.__string"
    """<p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>"""
    version: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInAppTemplateRequest) -> dict:
    out: dict = {}
    if "in_app_template_request" in value:
        import capo_pinpoint.types.in_app_template_request

        out["InAppTemplateRequest"] = (
            capo_pinpoint.types.in_app_template_request.serialize_json(
                value["in_app_template_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateInAppTemplateRequest:
    out: UpdateInAppTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("InAppTemplateRequest") is not None:
        import capo_pinpoint.types.in_app_template_request

        out["in_app_template_request"] = (
            capo_pinpoint.types.in_app_template_request.deserialize_json(
                data["InAppTemplateRequest"]
            )
        )
    return out

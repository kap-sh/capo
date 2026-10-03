"""Generated from Smithy shape ``com.amazonaws.oam#CreateLinkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_oam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_oam.types.label_template
    import capo_oam.types.link_configuration
    import capo_oam.types.resource_identifier
    import capo_oam.types.resource_types_input
    import capo_oam.types.tag_map_input


class CreateLinkInput(TypedDict, closed=True):
    label_template: "capo_oam.types.label_template.LabelTemplate"
    """<p>Specify a friendly human-readable name to use to identify this source account when you are viewing data from it in the monitoring account.</p> <p>You can use a custom label or use the following variables:</p> <ul> <li> <p> <code>$AccountName</code> is the name of the account</p> </li> <li> <p> <code>$AccountEmail</code> is the globally unique email address of the account</p> </li> <li> <p> <code>$AccountEmailNoDomain</code> is the email address of the account without the domain name</p> </li> </ul> <note> <p>In the Amazon Web Services GovCloud (US-East) and Amazon Web Services GovCloud (US-West) Regions, the only supported option is to use custom labels, and the <code>$AccountName</code>, <code>$AccountEmail</code>, and <code>$AccountEmailNoDomain</code> variables all resolve as <i>account-id</i> instead of the specified variable.</p> </note>"""
    resource_types: "capo_oam.types.resource_types_input.ResourceTypesInput"
    """<p>An array of strings that define which types of data that the source account shares with the monitoring account.</p>"""
    sink_identifier: "capo_oam.types.resource_identifier.ResourceIdentifier"
    """<p>The ARN of the sink to use to create this link. You can use <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html">ListSinks</a> to find the ARNs of sinks.</p> <p>For more information about sinks, see <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html">CreateSink</a>.</p>"""
    tags: NotRequired["capo_oam.types.tag_map_input.TagMapInput"]
    """<p>Assigns one or more tags (key-value pairs) to the link. </p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>For more information about using tags to control access, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html">Controlling access to Amazon Web Services resources using tags</a>.</p>"""
    link_configuration: NotRequired[
        "capo_oam.types.link_configuration.LinkConfiguration"
    ]
    """<p>Use this structure to optionally create filters that specify that only some metric namespaces or log groups are to be shared from the source account to the monitoring account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLinkInput) -> dict:
    out: dict = {}
    out["LabelTemplate"] = value["label_template"]
    import capo_oam.types.resource_types_input

    out["ResourceTypes"] = capo_oam.types.resource_types_input.serialize_json(
        value["resource_types"]
    )
    out["SinkIdentifier"] = value["sink_identifier"]
    if "tags" in value:
        import capo_oam.types.tag_map_input

        out["Tags"] = capo_oam.types.tag_map_input.serialize_json(value["tags"])
    if "link_configuration" in value:
        import capo_oam.types.link_configuration

        out["LinkConfiguration"] = capo_oam.types.link_configuration.serialize_json(
            value["link_configuration"]
        )
    return out


def deserialize_json(data: dict) -> CreateLinkInput:
    out: CreateLinkInput = {}  # type: ignore[typeddict-item]
    if data.get("LabelTemplate") is not None:
        out["label_template"] = data["LabelTemplate"]
    else:
        raise DeserializationError("CreateLinkInput.label_template required")
    if data.get("ResourceTypes") is not None:
        import capo_oam.types.resource_types_input

        out["resource_types"] = capo_oam.types.resource_types_input.deserialize_json(
            data["ResourceTypes"]
        )
    else:
        raise DeserializationError("CreateLinkInput.resource_types required")
    if data.get("SinkIdentifier") is not None:
        out["sink_identifier"] = data["SinkIdentifier"]
    else:
        raise DeserializationError("CreateLinkInput.sink_identifier required")
    if data.get("Tags") is not None:
        import capo_oam.types.tag_map_input

        out["tags"] = capo_oam.types.tag_map_input.deserialize_json(data["Tags"])
    if data.get("LinkConfiguration") is not None:
        import capo_oam.types.link_configuration

        out["link_configuration"] = capo_oam.types.link_configuration.deserialize_json(
            data["LinkConfiguration"]
        )
    return out

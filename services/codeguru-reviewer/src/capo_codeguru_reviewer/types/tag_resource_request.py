"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeguru_reviewer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.association_arn
    import capo_codeguru_reviewer.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_codeguru_reviewer.types.association_arn.AssociationArn"
    """<p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html">ListRepositoryAssociations</a>.</p>"""
    tags: "capo_codeguru_reviewer.types.tag_map.TagMap"
    """<p>An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts:</p> <ul> <li> <p>A <i>tag key</i> (for example, <code>CostCenter</code>, <code>Environment</code>, <code>Project</code>, or <code>Secret</code>). Tag keys are case sensitive.</p> </li> <li> <p>An optional field known as a <i>tag value</i> (for example, <code>111122223333</code>, <code>Production</code>, or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_codeguru_reviewer.types.tag_map

    out["Tags"] = capo_codeguru_reviewer.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_codeguru_reviewer.types.tag_map

        out["tags"] = capo_codeguru_reviewer.types.tag_map.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

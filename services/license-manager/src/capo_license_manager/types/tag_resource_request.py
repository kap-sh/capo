"""Generated from Smithy shape ``com.amazonaws.licensemanager#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string
    import capo_license_manager.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the resource. The following examples provide an example ARN for each supported resource in License Manager:</p> <ul> <li> <p>Licenses - <code>arn:aws:license-manager::111122223333:license:l-EXAMPLE2da7646d6861033667f20e895</code> </p> </li> <li> <p>Grants - <code>arn:aws:license-manager::111122223333:grant:g-EXAMPLE7b19f4a0ab73679b0beb52707</code> </p> </li> <li> <p>License configurations - <code>arn:aws:license-manager:us-east-1:111122223333:license-configuration:lic-EXAMPLE6a788d4c8acd4264ff0ecf2ed2d</code> </p> </li> <li> <p>Report generators - <code>arn:aws:license-manager:us-east-1:111122223333:report-generator:r-EXAMPLE825b4a4f8fe5a3e0c88824e5fc6</code> </p> </li> </ul>"""
    tags: "capo_license_manager.types.tag_list.TagList"
    """<p>One or more tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_license_manager.types.tag_list

    out["Tags"] = capo_license_manager.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_license_manager.types.tag_list

        out["tags"] = capo_license_manager.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out

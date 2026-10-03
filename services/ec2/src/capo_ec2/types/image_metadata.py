"""Generated from Smithy shape ``com.amazonaws.ec2#ImageMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.image_id
    import capo_ec2.types.image_state
    import capo_ec2.types.image_watermark_list
    import capo_ec2.types.string


class ImageMetadata(TypedDict, closed=True):
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the AMI.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the AMI.</p>"""
    state: NotRequired["capo_ec2.types.image_state.ImageState"]
    """<p>The current state of the AMI. If the state is <code>available</code>, the AMI is successfully registered and can be used to launch an instance.</p>"""
    image_owner_alias: NotRequired["capo_ec2.types.string.String"]
    """<p>The alias of the AMI owner.</p> <p>Valid values: <code>amazon</code> | <code>aws-backup-vault</code> | <code>aws-marketplace</code> </p>"""
    creation_date: NotRequired["capo_ec2.types.string.String"]
    """<p>The date and time the AMI was created.</p>"""
    deprecation_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The deprecation date and time of the AMI, in UTC, in the following format: <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z.</p>"""
    image_allowed: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, the AMI satisfies the criteria for Allowed AMIs and can be discovered and used in the account. If <code>false</code>, the AMI can't be discovered or used in the account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html">Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs</a> in <i>Amazon EC2 User Guide</i>.</p>"""
    is_public: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the AMI has public launch permissions. A value of <code>true</code> means this AMI has public launch permissions, while <code>false</code> means it has only implicit (AMI owner) or explicit (shared with your account) launch permissions.</p>"""
    image_watermarks: NotRequired[
        "capo_ec2.types.image_watermark_list.ImageWatermarkList"
    ]
    """<p>The watermarks attached to the AMI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageMetadata, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "owner_id" in value:
        pairs.append((f"{key_prefix}ImageOwnerId", str(value["owner_id"])))
    if "state" in value:
        import capo_ec2.types.image_state

        capo_ec2.types.image_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}ImageState"
        )
    if "image_owner_alias" in value:
        pairs.append((f"{key_prefix}ImageOwnerAlias", str(value["image_owner_alias"])))
    if "creation_date" in value:
        pairs.append((f"{key_prefix}CreationDate", str(value["creation_date"])))
    if "deprecation_time" in value:
        pairs.append((f"{key_prefix}DeprecationTime", str(value["deprecation_time"])))
    if "image_allowed" in value:
        pairs.append(
            (f"{key_prefix}ImageAllowed", "true" if value["image_allowed"] else "false")
        )
    if "is_public" in value:
        pairs.append(
            (f"{key_prefix}IsPublic", "true" if value["is_public"] else "false")
        )
    if "image_watermarks" in value:
        import capo_ec2.types.image_watermark_list

        capo_ec2.types.image_watermark_list.serialize_ec2_query(
            value["image_watermarks"], pairs, f"{key_prefix}ImageWatermarkSet"
        )


def deserialize_ec2_query(el: Element) -> ImageMetadata:
    out: ImageMetadata = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("imageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_name = el.find("name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_owner_id = el.find("imageOwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_state = el.find("imageState")
    if child_state is not None:
        import capo_ec2.types.image_state

        out["state"] = capo_ec2.types.image_state.deserialize_ec2_query(child_state)
    child_image_owner_alias = el.find("imageOwnerAlias")
    if child_image_owner_alias is not None:
        out["image_owner_alias"] = str(child_image_owner_alias.text or "")
    child_creation_date = el.find("creationDate")
    if child_creation_date is not None:
        out["creation_date"] = str(child_creation_date.text or "")
    child_deprecation_time = el.find("deprecationTime")
    if child_deprecation_time is not None:
        out["deprecation_time"] = str(child_deprecation_time.text or "")
    child_image_allowed = el.find("imageAllowed")
    if child_image_allowed is not None:
        out["image_allowed"] = (child_image_allowed.text or "").lower() == "true"
    child_is_public = el.find("isPublic")
    if child_is_public is not None:
        out["is_public"] = (child_is_public.text or "").lower() == "true"
    child_image_watermarks = el.find("imageWatermarkSet")
    if child_image_watermarks is not None:
        import capo_ec2.types.image_watermark_list

        out["image_watermarks"] = (
            capo_ec2.types.image_watermark_list.deserialize_ec2_query(
                child_image_watermarks
            )
        )
    return out

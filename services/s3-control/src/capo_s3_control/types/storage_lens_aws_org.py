"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensAwsOrg``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.aws_org_arn


class StorageLensAwsOrg(TypedDict, closed=True):
    arn: "capo_s3_control.types.aws_org_arn.AwsOrgArn"
    """<p>A container for the Amazon Resource Name (ARN) of the Amazon Web Services organization. This property is read-only and follows the following format: <code> arn:aws:organizations:<i>us-east-1</i>:<i>example-account-id</i>:organization/<i>o-ex2l495dck</i> </code> </p>"""


# --- restXml ser/de ---
def serialize_xml(value: StorageLensAwsOrg, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Arn").text = str(value["arn"])


def deserialize_xml(el: Element) -> StorageLensAwsOrg:
    out: StorageLensAwsOrg = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        out["arn"] = ""
    return out

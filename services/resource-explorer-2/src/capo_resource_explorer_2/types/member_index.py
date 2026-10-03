"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#MemberIndex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.index_type


class MemberIndex(TypedDict, closed=True):
    account_id: NotRequired["str"]
    """<p>The account ID for the index.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region in which the index exists.</p>"""
    arn: NotRequired["str"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the index.</p>"""
    type: NotRequired["capo_resource_explorer_2.types.index_type.IndexType"]
    """<p>The type of index. It can be one of the following values: </p> <ul> <li> <p> <code>LOCAL</code> – The index contains information about resources from only the same Amazon Web Services Region.</p> </li> <li> <p> <code>AGGREGATOR</code> – Resource Explorer replicates copies of the indexed information about resources in all other Amazon Web Services Regions to the aggregator index. This lets search results in the Region with the aggregator index to include resources from all Regions in the account where Resource Explorer is turned on.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberIndex) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "region" in value:
        out["Region"] = value["region"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> MemberIndex:
    out: MemberIndex = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out

"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#RollbackTrigger``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__string


class RollbackTrigger(TypedDict, closed=True):
    arn: NotRequired["capo_serverlessapplicationrepository.types.__string.__string"]
    """<p>This property corresponds to the content of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger">RollbackTrigger</a> </i> Data Type.</p>"""
    type: NotRequired["capo_serverlessapplicationrepository.types.__string.__string"]
    """<p>This property corresponds to the content of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger">RollbackTrigger</a> </i> Data Type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollbackTrigger) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> RollbackTrigger:
    out: RollbackTrigger = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out

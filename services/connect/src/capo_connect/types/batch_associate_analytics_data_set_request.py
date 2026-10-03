"""Generated from Smithy shape ``com.amazonaws.connect#BatchAssociateAnalyticsDataSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.aws_account_id
    import capo_connect.types.data_set_ids
    import capo_connect.types.instance_id


class BatchAssociateAnalyticsDataSetRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    data_set_ids: "capo_connect.types.data_set_ids.DataSetIds"
    """<p>An array of dataset identifiers to associate.</p>"""
    target_account_id: NotRequired["capo_connect.types.aws_account_id.AWSAccountId"]
    """<p>The identifier of the target account. Use to associate a dataset to a different account than the one containing the Connect Customer instance. If not specified, by default this value is the Amazon Web Services account that has the Connect Customer instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateAnalyticsDataSetRequest) -> dict:
    out: dict = {}
    import capo_connect.types.data_set_ids

    out["DataSetIds"] = capo_connect.types.data_set_ids.serialize_json(
        value["data_set_ids"]
    )
    if "target_account_id" in value:
        out["TargetAccountId"] = value["target_account_id"]
    return out


def deserialize_json(data: dict) -> BatchAssociateAnalyticsDataSetRequest:
    out: BatchAssociateAnalyticsDataSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("DataSetIds") is not None:
        import capo_connect.types.data_set_ids

        out["data_set_ids"] = capo_connect.types.data_set_ids.deserialize_json(
            data["DataSetIds"]
        )
    else:
        raise DeserializationError(
            "BatchAssociateAnalyticsDataSetRequest.data_set_ids required"
        )
    if data.get("TargetAccountId") is not None:
        out["target_account_id"] = data["TargetAccountId"]
    return out

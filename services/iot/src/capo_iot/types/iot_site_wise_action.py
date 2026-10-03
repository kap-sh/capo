"""Generated from Smithy shape ``com.amazonaws.iot#IotSiteWiseAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.put_asset_property_value_entry_list


class IotSiteWiseAction(TypedDict, closed=True):
    put_asset_property_value_entries: "capo_iot.types.put_asset_property_value_entry_list.PutAssetPropertyValueEntryList"
    """<p>A list of asset property value entries.</p>"""
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the role that grants IoT permission to send an asset property value to IoT SiteWise. (<code>"Action": "iotsitewise:BatchPutAssetPropertyValue"</code>). The trust policy can restrict access to specific asset hierarchy paths.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotSiteWiseAction) -> dict:
    out: dict = {}
    import capo_iot.types.put_asset_property_value_entry_list

    out["putAssetPropertyValueEntries"] = (
        capo_iot.types.put_asset_property_value_entry_list.serialize_json(
            value["put_asset_property_value_entries"]
        )
    )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> IotSiteWiseAction:
    out: IotSiteWiseAction = {}  # type: ignore[typeddict-item]
    if data.get("putAssetPropertyValueEntries") is not None:
        import capo_iot.types.put_asset_property_value_entry_list

        out["put_asset_property_value_entries"] = (
            capo_iot.types.put_asset_property_value_entry_list.deserialize_json(
                data["putAssetPropertyValueEntries"]
            )
        )
    else:
        raise DeserializationError(
            "IotSiteWiseAction.put_asset_property_value_entries required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("IotSiteWiseAction.role_arn required")
    return out

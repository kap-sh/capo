"""Generated from Smithy shape ``com.amazonaws.pi#FeatureMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.feature_status


class FeatureMetadata(TypedDict, closed=True):
    status: NotRequired["capo_pi.types.feature_status.FeatureStatus"]
    """<p>The status of the feature on the DB instance. Possible values include the following:</p> <ul> <li> <p> <code>ENABLED</code> - The feature is enabled on the instance.</p> </li> <li> <p> <code>DISABLED</code> - The feature is disabled on the instance.</p> </li> <li> <p> <code>UNSUPPORTED</code> - The feature isn't supported on the instance.</p> </li> <li> <p> <code>ENABLED_PENDING_REBOOT</code> - The feature is enabled on the instance but requires a reboot to take effect.</p> </li> <li> <p> <code>DISABLED_PENDING_REBOOT</code> - The feature is disabled on the instance but requires a reboot to take effect.</p> </li> <li> <p> <code>UNKNOWN</code> - The feature status couldn't be determined.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureMetadata) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_pi.types.feature_status

        out["Status"] = capo_pi.types.feature_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FeatureMetadata:
    out: FeatureMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_pi.types.feature_status

        out["status"] = capo_pi.types.feature_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FeatureMetadata) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_pi.types.feature_status

        out["Status"] = capo_pi.types.feature_status.serialize_cbor(value["status"])
    return out


def deserialize_cbor(data: dict) -> FeatureMetadata:
    out: FeatureMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_pi.types.feature_status

        out["status"] = capo_pi.types.feature_status.deserialize_cbor(data["Status"])
    return out

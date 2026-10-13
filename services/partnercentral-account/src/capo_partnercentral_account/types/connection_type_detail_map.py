"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionTypeDetailMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_account.types.connection_type
    import capo_partnercentral_account.types.connection_type_detail

ConnectionTypeDetailMap: TypeAlias = dict[
    "capo_partnercentral_account.types.connection_type.ConnectionType",
    "capo_partnercentral_account.types.connection_type_detail.ConnectionTypeDetail",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ConnectionTypeDetailMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_partnercentral_account.types.connection_type
        import capo_partnercentral_account.types.connection_type_detail

        out[
            capo_partnercentral_account.types.connection_type.serialize_aws_json_1_0(
                key
            )
        ] = capo_partnercentral_account.types.connection_type_detail.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectionTypeDetailMap:
    out: ConnectionTypeDetailMap = {}
    for key, value in data.items():
        import capo_partnercentral_account.types.connection_type

        if value is None:
            continue
        import capo_partnercentral_account.types.connection_type_detail

        out[
            capo_partnercentral_account.types.connection_type.deserialize_aws_json_1_0(
                key
            )
        ] = capo_partnercentral_account.types.connection_type_detail.deserialize_aws_json_1_0(
            value
        )
    return out


def redact_sensitive(value: ConnectionTypeDetailMap) -> dict[str, Any]:
    import capo_partnercentral_account.types.connection_type_detail

    return {
        key: capo_partnercentral_account.types.connection_type_detail.redact_sensitive(
            item
        )
        for key, item in value.items()
    }

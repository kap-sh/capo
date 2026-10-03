"""Generated from Smithy shape ``com.amazonaws.acm#Filters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.certificate_export
    import capo_acm.types.certificate_managed_by
    import capo_acm.types.extended_key_usage_filter_list
    import capo_acm.types.key_algorithm_list
    import capo_acm.types.key_usage_filter_list


class Filters(TypedDict, closed=True):
    extended_key_usage: NotRequired[
        "capo_acm.types.extended_key_usage_filter_list.ExtendedKeyUsageFilterList"
    ]
    """<p>Specify one or more <a>ExtendedKeyUsage</a> extension values.</p>"""
    key_usage: NotRequired["capo_acm.types.key_usage_filter_list.KeyUsageFilterList"]
    """<p>Specify one or more <a>KeyUsage</a> extension values.</p>"""
    key_types: NotRequired["capo_acm.types.key_algorithm_list.KeyAlgorithmList"]
    """<p>Specify one or more algorithms that can be used to generate key pairs.</p> <p>Default filtering returns only <code>RSA_1024</code> and <code>RSA_2048</code> certificates that have at least one domain. To return other certificate types, provide the desired type signatures in a comma-separated list. For example, <code>"keyTypes": ["RSA_2048","RSA_4096"]</code> returns both <code>RSA_2048</code> and <code>RSA_4096</code> certificates.</p>"""
    export_option: NotRequired["capo_acm.types.certificate_export.CertificateExport"]
    """<p>Specify <code>ENABLED</code> or <code>DISABLED</code> to identify certificates that can be exported.</p>"""
    managed_by: NotRequired[
        "capo_acm.types.certificate_managed_by.CertificateManagedBy"
    ]
    """<p>Identifies the Amazon Web Services service that manages the certificate issued by ACM.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filters) -> dict:
    out: dict = {}
    if "extended_key_usage" in value:
        import capo_acm.types.extended_key_usage_filter_list

        out["extendedKeyUsage"] = (
            capo_acm.types.extended_key_usage_filter_list.serialize_aws_json_1_1(
                value["extended_key_usage"]
            )
        )
    if "key_usage" in value:
        import capo_acm.types.key_usage_filter_list

        out["keyUsage"] = capo_acm.types.key_usage_filter_list.serialize_aws_json_1_1(
            value["key_usage"]
        )
    if "key_types" in value:
        import capo_acm.types.key_algorithm_list

        out["keyTypes"] = capo_acm.types.key_algorithm_list.serialize_aws_json_1_1(
            value["key_types"]
        )
    if "export_option" in value:
        import capo_acm.types.certificate_export

        out["exportOption"] = capo_acm.types.certificate_export.serialize_aws_json_1_1(
            value["export_option"]
        )
    if "managed_by" in value:
        import capo_acm.types.certificate_managed_by

        out["managedBy"] = capo_acm.types.certificate_managed_by.serialize_aws_json_1_1(
            value["managed_by"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filters:
    out: Filters = {}  # type: ignore[typeddict-item]
    if data.get("extendedKeyUsage") is not None:
        import capo_acm.types.extended_key_usage_filter_list

        out["extended_key_usage"] = (
            capo_acm.types.extended_key_usage_filter_list.deserialize_aws_json_1_1(
                data["extendedKeyUsage"]
            )
        )
    if data.get("keyUsage") is not None:
        import capo_acm.types.key_usage_filter_list

        out["key_usage"] = (
            capo_acm.types.key_usage_filter_list.deserialize_aws_json_1_1(
                data["keyUsage"]
            )
        )
    if data.get("keyTypes") is not None:
        import capo_acm.types.key_algorithm_list

        out["key_types"] = capo_acm.types.key_algorithm_list.deserialize_aws_json_1_1(
            data["keyTypes"]
        )
    if data.get("exportOption") is not None:
        import capo_acm.types.certificate_export

        out["export_option"] = (
            capo_acm.types.certificate_export.deserialize_aws_json_1_1(
                data["exportOption"]
            )
        )
    if data.get("managedBy") is not None:
        import capo_acm.types.certificate_managed_by

        out["managed_by"] = (
            capo_acm.types.certificate_managed_by.deserialize_aws_json_1_1(
                data["managedBy"]
            )
        )
    return out

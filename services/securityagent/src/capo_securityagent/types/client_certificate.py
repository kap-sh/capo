"""Generated from Smithy shape ``com.amazonaws.securityagent#ClientCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.client_certificate_name
    import capo_securityagent.types.client_certificate_origin_list


class ClientCertificate(TypedDict, closed=True):
    name: "capo_securityagent.types.client_certificate_name.ClientCertificateName"
    """<p>A customer-chosen name for this client certificate, used in error messages and console display.</p>"""
    secret_arn: "str"
    """<p>The ARN of the Secrets Manager secret containing the certificate and private key.</p>"""
    origins: "capo_securityagent.types.client_certificate_origin_list.ClientCertificateOriginList"
    """<p>The origins (scheme://host[:port]) this certificate applies to. Paths are not supported. Each hostname can have at most one client certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientCertificate) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["secretArn"] = value["secret_arn"]
    import capo_securityagent.types.client_certificate_origin_list

    out["origins"] = (
        capo_securityagent.types.client_certificate_origin_list.serialize_json(
            value["origins"]
        )
    )
    return out


def deserialize_json(data: dict) -> ClientCertificate:
    out: ClientCertificate = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        out["secret_arn"] = ""
    if data.get("origins") is not None:
        import capo_securityagent.types.client_certificate_origin_list

        out["origins"] = (
            capo_securityagent.types.client_certificate_origin_list.deserialize_json(
                data["origins"]
            )
        )
    else:
        out["origins"] = []
    return out

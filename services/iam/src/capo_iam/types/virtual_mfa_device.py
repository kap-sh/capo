"""Generated from Smithy shape ``com.amazonaws.iam#VirtualMFADevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.bootstrap_datum
    import capo_iam.types.date_type
    import capo_iam.types.serial_number_type
    import capo_iam.types.tag_list_type
    import capo_iam.types.user


class VirtualMFADevice(TypedDict, closed=True):
    serial_number: "capo_iam.types.serial_number_type.serialNumberType"
    """<p>The serial number associated with <code>VirtualMFADevice</code>.</p>"""
    base32_string_seed: NotRequired["capo_iam.types.bootstrap_datum.BootstrapDatum"]
    """<p> The base32 seed defined as specified in <a href="https://tools.ietf.org/html/rfc3548.txt">RFC3548</a>. The <code>Base32StringSeed</code> is base32-encoded. </p>"""
    qr_code_png: NotRequired["capo_iam.types.bootstrap_datum.BootstrapDatum"]
    """<p> A QR code PNG image that encodes <code>otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String</code> where <code>$virtualMFADeviceName</code> is one of the create call arguments. <code>AccountName</code> is the user name if set (otherwise, the account ID otherwise), and <code>Base32String</code> is the seed in base32 format. The <code>Base32String</code> value is base64-encoded. </p>"""
    user: NotRequired["capo_iam.types.user.User"]
    """<p>The IAM user associated with this virtual MFA device.</p>"""
    enable_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time on which the virtual MFA device was enabled.</p>"""
    tags: NotRequired["capo_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that are attached to the virtual MFA device. For more information about tagging, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VirtualMFADevice, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}SerialNumber", str(value["serial_number"])))
    if "base32_string_seed" in value:
        import capo_iam.types.bootstrap_datum

        capo_iam.types.bootstrap_datum.serialize_query(
            value["base32_string_seed"], pairs, f"{key_prefix}Base32StringSeed"
        )
    if "qr_code_png" in value:
        import capo_iam.types.bootstrap_datum

        capo_iam.types.bootstrap_datum.serialize_query(
            value["qr_code_png"], pairs, f"{key_prefix}QRCodePNG"
        )
    if "user" in value:
        import capo_iam.types.user

        capo_iam.types.user.serialize_query(value["user"], pairs, f"{key_prefix}User")
    if "enable_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["enable_date"], pairs, f"{key_prefix}EnableDate"
        )
    if "tags" in value:
        import capo_iam.types.tag_list_type

        capo_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> VirtualMFADevice:
    out: VirtualMFADevice = {}  # type: ignore[typeddict-item]
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError("VirtualMFADevice.serial_number required")
    child_base32_string_seed = el.find("Base32StringSeed")
    if child_base32_string_seed is not None:
        import capo_iam.types.bootstrap_datum

        out["base32_string_seed"] = capo_iam.types.bootstrap_datum.deserialize_query(
            child_base32_string_seed
        )
    child_qr_code_png = el.find("QRCodePNG")
    if child_qr_code_png is not None:
        import capo_iam.types.bootstrap_datum

        out["qr_code_png"] = capo_iam.types.bootstrap_datum.deserialize_query(
            child_qr_code_png
        )
    child_user = el.find("User")
    if child_user is not None:
        import capo_iam.types.user

        out["user"] = capo_iam.types.user.deserialize_query(child_user)
    child_enable_date = el.find("EnableDate")
    if child_enable_date is not None:
        import capo_iam.types.date_type

        out["enable_date"] = capo_iam.types.date_type.deserialize_query(
            child_enable_date
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    return out

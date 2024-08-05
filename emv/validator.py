from typing import Union
from .model import ValidatedEmail
from emv import _emv


class EmailValidator:
    """
    Initializes an EmailValidator object.


    Args:
        email (Union[str, bytes]): The email address to validate.
        allow_smtputf8 (bool): Whether to allow SMTPUTF8. Default is True.
        allow_empty_local (bool): Whether to allow empty local part. \
        Default is False.
        allow_quoted_local (bool): Whether to allow quoted local part. \
        Default is False.
        allow_domain_literal (bool): Whether to allow domain literals. \
        Default is False.
        deliverable_address (bool): Whether to check if the email address is \
        deliverable. Default is True.

    """

    def __init__(
        self,
        allow_smtputf8: bool = True,
        allow_empty_local: bool = False,
        allow_quoted_local: bool = False,
        allow_domain_literal: bool = False,
        deliverable_address: bool = True,
    ):
        self._emv = _emv.EmailValidator(
            allow_smtputf8,
            allow_empty_local,
            allow_quoted_local,
            allow_domain_literal,
            deliverable_address,
        )

    def validate_email(self, email: Union[str, bytes]) -> ValidatedEmail:
        """
        Validates an email address.

        Args:
            email: The email address to validate.

        Returns:
            A ValidatedEmail instance if the email is valid.

        Raises:
            SyntaxError: If the email syntax is invalid.
            DomainLiteralError: If domain literals are not allowed.
            LengthError: If the email length exceeds the maximum allowed length.
        """
        validated_email = self._emv.validate_email(email)
        return ValidatedEmail(
            original=validated_email.original,
            normalized=validated_email.normalized,
            local_part=validated_email.local_part,
            domain_name=validated_email.domain_name,
            domain_address=validated_email.domain_address,
        )


def validate_email(
    email: Union[str, bytes],
    allow_smtputf8: bool = True,
    allow_empty_local: bool = False,
    allow_quoted_local: bool = False,
    allow_domain_literal: bool = False,
    deliverable_address: bool = True,
) -> ValidatedEmail:
    """
    Validates an email address with optional parameters.

    Args:
        email (Union[str, bytes]): The email address to validate.
        allow_smtputf8 (bool): Whether to allow SMTPUTF8. Default is True.
        allow_empty_local (bool): Whether to allow empty local part. \
        Default is False.
        allow_quoted_local (bool): Whether to allow quoted local part. \
        Default is False.
        allow_domain_literal (bool): Whether to allow domain literals. \
        Default is False.
        deliverable_address (bool): Whether to check if the email address is \
        deliverable. Default is True.

    Returns:
        ValidatedEmail: An instance if the email is valid.
    """
    emv = EmailValidator(
        allow_smtputf8,
        allow_empty_local,
        allow_quoted_local,
        allow_domain_literal,
        deliverable_address,
    )
    return emv.validate_email(email)

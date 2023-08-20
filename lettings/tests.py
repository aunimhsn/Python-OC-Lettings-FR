import pytest
from .models import Address


@pytest.fixture
def addresses():
    return Address.objects.get_or_create(
        number=808,
        street='Winchester Avenue',
        city='Chicago',
        state='OH',
        zip_code=41233,
        country_iso_code='USA'
    )


@pytest.mark.django_db(transaction=True)
def test_addresses_count(addresses):
    assert Address.objects.count() == 1
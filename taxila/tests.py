from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from taxila.models import Material, MaterialCategory, MetaData, ParentCategory


class HomepageAPIViewTest(APITestCase):
    def test_get_success(self) -> None:
        url = reverse("homepage")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BannerImagesAPIViewTest(APITestCase):
    def test_get_success(self) -> None:
        url = reverse("banners-images")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class KitchenCategoryAPIViewTest(APITestCase):
    def test_get_success(self) -> None:
        url = reverse("kitchen-category")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MaterialCategoryAPIViewTest(APITestCase):
    def test_get_success(self) -> None:
        url = reverse("material-category")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class VideoCategoryAPIViewTest(APITestCase):
    def test_get_success(self) -> None:
        url = reverse("video-category")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MediaCategoryAPIViewTest(APITestCase):
    def test_get_success(self) -> None:
        url = reverse("media-category")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class InspirationCategoryAPIViewTest(APITestCase):
    def test_get_success(self) -> None:
        url = reverse("inspiration-category")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class VideosAPIViewTest(APITestCase):
    def test_get_success(self) -> None:
        url = reverse("videos")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MediaAPIViewTest(APITestCase):
    def test_get_success(self) -> None:
        url = reverse("media")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class InspirationAPIViewTest(APITestCase):
    def test_get_success(self) -> None:
        url = reverse("inspiration")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class KitchenAPIViewTest(APITestCase):
    def test_get_success(self) -> None:
        url = reverse("kitchen")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MetadataAPIViewTest(APITestCase):
    def setUp(self) -> None:
        MetaData.objects.get_or_create(
            slug="some-slug",
            title="some-title",
            meta_description="some-meta_description",
            og_title="some-og_title",
            og_description="some-og_description",
            twitter_title="some-twitter_title",
            twitter_description="some-twitter_description",
        )
        return super().setUp()

    def test_get_success(self) -> None:
        url = reverse("meta-data", kwargs={"slug": "some-slug"})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "some-title")
        self.assertEqual(response.data["script"], {})

    def test_get_not_found(self) -> None:
        url = reverse("meta-data", kwargs={"slug": "yet-another-slug"})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ParentMaterialDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        ParentCategory.objects.get_or_create(
            id=1,
            name="Some Name",
            slug="some-name",
        )
        return super().setUp()

    def test_get_success(self) -> None:
        url = reverse("parent-material", kwargs={"id": 1})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_not_found(self) -> None:
        url = reverse("parent-material", kwargs={"id": 2})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class MaterialDetailAPIViewTest(APITestCase):
    def setUp(self) -> None:
        pc = ParentCategory.objects.get_or_create(name="some-name")[0]
        mc = MaterialCategory.objects.get_or_create(name="some-name", parent_category=pc)[0]
        Material.objects.get_or_create(
            id=1,
            slug="some-slug",
            name="some-name",
            category=mc,
        )
        return super().setUp()

    def test_get_success(self) -> None:
        url = reverse("material-detail", kwargs={"query": "1"})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MaterialAPIViewTest(APITestCase):
    def test_get_success(self) -> None:
        url = reverse("material")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SlugVerifyAPIViewTest(APITestCase):
    def setUp(self) -> None:
        pc = ParentCategory.objects.get_or_create(name="some-name")[0]
        mc = MaterialCategory.objects.get_or_create(name="some-name", parent_category=pc)[0]
        Material.objects.get_or_create(
            id=1,
            slug="some-slug",
            name="some-name",
            category=mc,
        )
        return super().setUp()

    def test_get_success_true(self) -> None:
        url = reverse("slug-verify", kwargs={"slug": "some-slug"})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["exists"], True)

    def test_get_success_false(self) -> None:
        url = reverse("slug-verify", kwargs={"slug": "yet-another-slug"})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["exists"], False)

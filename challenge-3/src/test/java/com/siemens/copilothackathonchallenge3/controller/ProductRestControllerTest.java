package com.siemens.copilothackathonchallenge3.controller;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;
import com.siemens.copilothackathonchallenge3.entity.Product;
import com.siemens.copilothackathonchallenge3.service.ProductService;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import java.util.Arrays;
import java.util.List;

import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
public class ProductRestControllerTest {

    @InjectMocks
    private ProductRestController productRestController;

    @Mock
    private ProductService productService;

    private MockMvc mockMvc;
    private ObjectMapper objectMapper = new ObjectMapper();
    private ObjectWriter objectWriter = objectMapper.writer().withDefaultPrettyPrinter();

    @Test
    public void testGetAllProducts() throws Exception {
        // Arrange
        Product product1 = new Product();
        product1.setId(1l);
        product1.setName("Product 1");
        product1.setDescription("Description 1");
        product1.setPrice(10.0);
        Product product2 = new Product();
        product2.setId(2l);
        product2.setName("Product 2");
        product2.setDescription("Description 2");
        product2.setPrice(20.0);
        List<Product> products = Arrays.asList(product1, product2);
        when(productService.getAllProducts()).thenReturn(products);

        mockMvc = MockMvcBuilders.standaloneSetup(productRestController).build();

        // Act & Assert
        mockMvc.perform(MockMvcRequestBuilders.get("/api/items"))
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andExpect(MockMvcResultMatchers.content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(MockMvcResultMatchers.jsonPath("$[0].id").value("1"))
                .andExpect(MockMvcResultMatchers.jsonPath("$[0].name").value("Product 1"))
                .andExpect(MockMvcResultMatchers.jsonPath("$[1].id").value("2"))
                .andExpect(MockMvcResultMatchers.jsonPath("$[1].name").value("Product 2"));
    }

    @Test
    public void testGetProductById() throws Exception {
        // Arrange
        Product product = new Product();
        product.setId(1l);
        product.setName("Product 1");
        product.setDescription("Description 1");
        product.setPrice(10.0);
        when(productService.getProductById(1l)).thenReturn(product);

        mockMvc = MockMvcBuilders.standaloneSetup(productRestController).build();

        // Act & Assert
        mockMvc.perform(MockMvcRequestBuilders.get("/api/items/1"))
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andExpect(MockMvcResultMatchers.content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(MockMvcResultMatchers.jsonPath("$.id").value("1"))
                .andExpect(MockMvcResultMatchers.jsonPath("$.name").value("Product 1"));
    }

    @Test
    public void testCreateProduct() throws Exception {
        // Arrange
        Product productToCreate = new Product(null, "New Product", "New Description", 30.0); // ID null for new product
        Product createdProduct = new Product(3l, "New Product", "New Description", 30.0); // ID assigned after creation
        when(productService.saveProduct(any(Product.class))).thenReturn(createdProduct); // Use any() matcher

        String json = objectWriter.writeValueAsString(productToCreate);
        mockMvc = MockMvcBuilders.standaloneSetup(productRestController).build();

        // Act & Assert
        mockMvc.perform(MockMvcRequestBuilders.post("/api/items")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(json))
                .andExpect(MockMvcResultMatchers.status().isOk()) // Or .isCreated(201) if you prefer
                .andExpect(MockMvcResultMatchers.jsonPath("$.id").value("3"))
                .andExpect(MockMvcResultMatchers.jsonPath("$.name").value("New Product"));
    }


    @Test
    public void testUpdateProduct() throws Exception {
        // Arrange
        Long id = 1l;
        Product existingProduct = new Product(id, "Product 1", "Description 1", 10.0);
        Product updatedProductDetails = new Product(null, "Updated Product", "Updated Description", 40.0); // ID is ignored in update
        Product updatedProduct = new Product(id, "Updated Product", "Updated Description", 40.0);
        when(productService.getProductById(id)).thenReturn(existingProduct);
        when(productService.saveProduct(any(Product.class))).thenReturn(updatedProduct);

        String json = objectWriter.writeValueAsString(updatedProductDetails);
        mockMvc = MockMvcBuilders.standaloneSetup(productRestController).build();

        // Act & Assert
        mockMvc.perform(MockMvcRequestBuilders.put("/api/items/" + id)
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(json))
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andExpect(MockMvcResultMatchers.jsonPath("$.id").value(id))
                .andExpect(MockMvcResultMatchers.jsonPath("$.name").value("Updated Product"));
    }

    @Test
    public void testDeleteProduct() throws Exception {
        // Arrange
        String id = "1";
        mockMvc = MockMvcBuilders.standaloneSetup(productRestController).build();

        // Act & Assert
        mockMvc.perform(MockMvcRequestBuilders.delete("/api/items/" + id))
                .andExpect(MockMvcResultMatchers.status().isNoContent()); // 204 No Content

        verify(productService, times(1)).deleteProduct(Long.valueOf(id)); // Verify that the service method was called
    }
}
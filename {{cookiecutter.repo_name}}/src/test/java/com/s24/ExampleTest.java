package com.s24;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class ExampleTest {

    @Test
    public void testGetGreeting() throws Exception {
        Example ex = new Example();
        assertEquals("Hello, world", ex.getGreeting());
    }
}

package org.euvsvirus.controller;

import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class IndexController implements ErrorController{

    private static final String PATH = "/error";

    @RequestMapping(value = PATH)
    public String error() {
        return "This is the research portal API endpoint of University Medical Centre Maribor, Slovenia.";
    }

    @Override
    public String getErrorPath() {
        return PATH;
    }
}

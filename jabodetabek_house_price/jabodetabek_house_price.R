# Prepare the necessary packages and libraries
if(!require(shiny)) install.packages("shiny")
if(!require(shinydashboard)) install.packages("shinydashboard")
if(!require(shinyBS)) install.packages("shinyBS")
if(!require(shinyWidgets)) install.packages("shinyWidgets")
if(!require(readr)) install.packages("readr")
if(!require(dplyr)) install.packages("dplyr")
if(!require(sf)) install.packages("sf")
if(!require(htmlwidgets)) install.packages("htmlwidgets")
if(!require(leaflet)) install.packages("leaflet")
if(!require(ggplot2)) install.packages("ggplot2")

# Call the packages and libraries
library(shiny)
library(shinydashboard)
library(shinyBS)
library(shinyWidgets)
library(readr)
library(dplyr)
library(sf)
library(htmlwidgets)
library(leaflet)
library(ggplot2)

# Set working directory
setwd("robiatulaa/jabodetabek_house_price")

# Read the csv main file that contains Jabodetabek house price data
jabodetabek_house_price <- read_csv("jabodetabek_house_price_cleaned.csv")
jabodetabek_house_price$city <- toupper(jabodetabek_house_price$city)

# Define UI
ui <- dashboardPage(
  dashboardHeader(title = tags$div("HOUSE PRICES IN THE JABODETABEK AREA",
                                   id = "title", style = "font-weight: bold; font-size: 25px;"),
                  titleWidth = "100%"), # Place the title in the middle of the dashboard
  
  # Deactivate the dashboard menu 
  dashboardSidebar(disable = TRUE),
  
  # Set the dashboard display
  dashboardBody(
    
    fluidRow(
      
      box(title = "Welcome to Our Interactive Dashboard!",
          status = "primary",
          width = 12,
          solidHeader = TRUE,
          collapsible = TRUE,
          collapsed = TRUE,
          "Explore the dynamic landscape of housing prices in the Jabodetabek area with our interactive dashboard.",
          "This tool is designed to provide you with comprehensive insights into the housing market, featuring four key visualizations:",
          "house location, condition, property attributes, and facilities.",
          "Get ready to meet your house!"),
    ),
    
    fluidRow(
      valueBoxOutput("sum_city", width = 3),
      valueBoxOutput("sum_num_house", width = 3),
      valueBoxOutput("sum_avg", width = 3),
      valueBoxOutput("sum_med", width = 3),
    ),
      
    fluidRow(
      
      box(title = tags$div("Spatial Patterns of House Prices in Jabodetabek",
                           id = "sphpj", style = "cursor: pointer; color: steelblue;"),
          width = 6,
          solidHeader = TRUE,
          leafletOutput("choropleth_map", height = "528px")),
      
      bsPopover(id = "sphpj", title = "Choropleth Map Information", 
                content = "In this map, you can see spatial patterns of house prices in Jabodetabek. When you klik the colored area in map, the pop up about the area information will appear. The color is based on median of house price in its area (look at the legend).", 
                placement = "bottom", 
                trigger = "click"),
      
      box(title = tags$div("House Price based on Condition Analysis",
                           id = "hpca", style = "cursor: pointer; color: steelblue;"),
          width = 4,
          solidHeader = TRUE,
          plotOutput("bar_chart", height = "185px")),
      
      bsPopover(id = "hpca", title = "Bar Chart Information", 
                content = "The bar chart shows the median price of house for sale in Jabodetabek area based on the house condition. The dropdown is provided, so you can choose which city information you want to know.", 
                placement = "bottom", 
                trigger = "click"),
      
      box(title = tags$div("Select the City :", style = "cursor: pointer; color: steelblue;"),
          width = 2,
          solidHeader = TRUE,
          radioGroupButtons(inputId = "select_city", 
                            choices = c("ALL (JABODETABEK)",
                                        "JAKARTA PUSAT",
                                        "JAKARTA SELATAN",
                                        "JAKARTA UTARA",
                                        "JAKARTA BARAT",
                                        "JAKARTA TIMUR",
                                        "BOGOR",
                                        "DEPOK",
                                        "TANGERANG",
                                        "BEKASI"),
                            size = "xs",
                            checkIcon = list(yes = icon("check", lib = "glyphicon")))),
      
      box(title = tags$div("House Price vs Property Attributes",
                           id = "hppa", style = "cursor: pointer; color: steelblue;"),
          width = 3,
          solidHeader = TRUE,
          selectInput("select_property_attribute", "Property Attribute Type :",
                      c("Land Size (m2)" = "land_size_m2", 
                        "Building Size (m2)" = "building_size_m2",
                        "Electricity Source (mAh)" = "electricity",
                        "Number of Bedrooms" = "bedrooms",
                        "Number of Bathrooms" = "bathrooms")),
          plotOutput("scatter_plot", height = "185px")),
      
      bsPopover(id = "hppa", title = "Scatter Plot Information", 
                content = "You can know the data distribution of house and its property attributes in the Jabodetabek with this scatter plot. The type of each property attribute is separated, but you can adjust it in the Select Property Attributes.", 
                placement = "bottom", 
                trigger = "click"),
      
      box(title = tags$div("House Price vs Facilities",
                           id = "hpf", style = "cursor: pointer; color: steelblue;"),
          width = 3,
          solidHeader = TRUE,
          selectInput("select_facility", "Facility Type :",
                      c("Furnishing" = "furnishing",
                        "Swimming Pool" = "swimming_pool",
                        "Parks" = "park",
                        "Jogging Track" = "jogging_track")),
          plotOutput("box_plot", height = "185px")),
      
      bsPopover(id = "hpf", title = "Box Plot Information", 
                content = "This box plot present the price distribution of a house based on its facility. There are 4 facilities in this visualization that can be chosen via Select Faciliy bellow.", 
                placement = "bottom", 
                trigger = "click")
    ),
    
    fluidRow(
      
      box(width = 12,
          solidHeader = TRUE,
          fluidRow(
            column(width = 10,
                  "The dashboard is made by Robiatul Adawiyah Al-Qosh (34269193) as the result of ITI5147 data exploration and visualisation assessment 3 final project.", tags$br(),
                  "The initial data for this visualization was got from : ",
                   tags$a(href = "https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek?select=jabodetabek_house_price.csv",
                         "Jabodetabek House Price")),
            column(width = 2,
                   tags$img(src = "https://jmeducationgroup.com/wp-content/uploads/2021/03/Monash-university-logo.png",
                            height = 38,
                            width = 140)),
          
        )
      )
    )
  )
)

# Define server
server <- function(input, output, session) {
  
  # Summary City
  output$sum_city <- renderValueBox({
    sum_city <- input$select_city
    valueBox(tags$div(sum_city, style = "font-size: 28px;"),
             "City",
             icon = icon("city"), color = "light-blue")
  })
  
  #Summary Number of House
  output$sum_num_house <- renderValueBox({
    if (input$select_city == "ALL (JABODETABEK)") {
      sum_num_house <- jabodetabek_house_price %>%
        summarise(house_quantity = format(n(), big.mark = ","))
    }
    else {
      sum_num_house <- jabodetabek_house_price %>%
        filter(city == input$select_city) %>%
        summarise(house_quantity = format(n(), big.mark = ","))
    }
    valueBox(tags$div(sum_num_house, style = "font-size: 28px;"),
             "Number of House for Sale",
             icon = icon("house"), color = "light-blue")
  })
  
  #Summary Average House Price
  output$sum_avg <- renderValueBox({
    if (input$select_city == "ALL (JABODETABEK)") {
      sum_avg <- jabodetabek_house_price %>%
        summarise(sum_avg = paste("IDR", format(round(mean(price_in_rp)), big.mark = ",", scientific = FALSE)))
    }
    else {
      sum_avg <- jabodetabek_house_price %>%
        filter(city == input$select_city) %>%
        summarise(sum_avg = paste("IDR", format(round(mean(price_in_rp)), big.mark = ",", scientific = FALSE)))
    }
    valueBox(tags$div(sum_avg, style = "font-size: 28px;"),
             "Average House Price",
             icon = icon("magnifying-glass-dollar"), color = "light-blue")
  })
  
  #Summary Median House Price
  output$sum_med <- renderValueBox({
    if (input$select_city == "ALL (JABODETABEK)") {
      sum_med <- jabodetabek_house_price %>%
        summarise(sum_med = paste("IDR", format(round(median(price_in_rp)), big.mark = ",", scientific = FALSE)))
    }
    else {
      sum_med <- jabodetabek_house_price %>%
        filter(city == input$select_city) %>%
        summarise(sum_med = paste("IDR", format(round(median(price_in_rp)), big.mark = ",", scientific = FALSE)))
    }
    valueBox(tags$div(sum_med, style = "font-size: 28px;"),
             "Median House Price",
             icon = icon("filter-circle-dollar"), color = "light-blue")
  })
  
  # CHOROPLETH MAP CHART
  output$choropleth_map <- renderLeaflet({
    
    # Read the SHP file to create the map chart
    jabodetabek <- st_read("BATAS KABUPATEN KOTA DESEMBER 2019 DUKCAPIL/BATAS KABUPATEN KOTA DESEMBER 2019 DUKCAPIL NEW.shp")
    
    # Make a new table about median price of house in each sub-region in Jabodetabek
    # The use of median values rather than averages to avoid data imbalances caused by outliers
    house_price_per_city <- jabodetabek_house_price %>%
      group_by(city) %>%
      summarise(med_house_price = median(price_in_rp),
                house_quantity = n())
    
    # Join the new table with SHP file
    names(jabodetabek)[names(jabodetabek) == "KAB_KOTA"] <- "city"
    house_price_per_city <- merge(jabodetabek, house_price_per_city, by = "city")
    
    # Create a color palette for the map based on the quantile
    pal <- colorQuantile("Blues", domain = house_price_per_city$med_house_price, n = 5)
    
    # Create the choropleth map
    map <- leaflet(data = house_price_per_city) %>%
      addTiles() %>%
      addProviderTiles("CartoDB.Positron") %>%
      addPolygons(
        fillColor = ~pal(med_house_price),
        fillOpacity = 0.7,
        color = "white",
        weight = 1.5,
        
        
        # Adding label for the city in map
        popup = ~paste(city, "<br>",
                       "Median House Price :", paste("IDR", round(med_house_price/1000000), "M",
                       "<br>", "House Quantity :", house_quantity)),
        popupOptions = popupOptions(
          maxWidth = 200,
          closeButton = TRUE,
          closeOnClick = TRUE,
          autoClose = TRUE
        ),
        highlight = highlightOptions(
          weight = 1.5,
          color = "lightskyblue",
          fillOpacity = 5,
          bringToFront = TRUE
        ),
      ) %>%
      
      # Adding legend into map
      addLegend(
        pal = pal,
        values = ~med_house_price,
        title = "Median Price (IDR)",
        position = "bottomright",
        labFormat = function(type, cuts, p) { 
          n = length(cuts)
          cuts = round(cuts/1000000)
          paste0(cuts[-n], "M - ", cuts[-1], "M")
        },
      )
  })
  
  # BAR CHART
  output$bar_chart <- renderPlot({
    
    # Managing the data for selected city
    if (input$select_city == "ALL (JABODETABEK)") {
      condition_per_city <- jabodetabek_house_price %>%
        group_by(property_condition) %>%
        summarise(med_condition = median(price_in_rp),
                  house_quantity = n()) %>%
        ungroup()
    }
    else {
      condition_per_city <- jabodetabek_house_price %>%
        filter(city == input$select_city) %>%
        group_by(property_condition, city) %>%
        summarise(med_condition = median(price_in_rp),
                  house_quantity = n()) %>%
        ungroup()
    }
    
    # Create the bar chart
    ggplot(condition_per_city,
           aes(x = reorder(property_condition, -med_condition))) +
               #y = med_condition,
               #fill = reorder(property_condition, med_condition))) + 
      geom_bar(aes(y = med_condition),
               fill = "lightskyblue1",
               stat="identity") + 
      geom_line(aes(y = house_quantity*max(condition_per_city$med_condition)/max(condition_per_city$house_quantity), group = 1),
                color = "lightskyblue4", size = 1) +
      geom_point(aes(y = house_quantity*max(condition_per_city$med_condition)/max(condition_per_city$house_quantity)),
                 color = "lightskyblue4", size = 2) +
      labs(x = "House Condition") +
      scale_y_continuous(name = "House Price (IDR in Million)",
                         labels = function(x) paste0(x/1000000),
                         sec.axis = sec_axis(~.*max(condition_per_city$house_quantity)/max(condition_per_city$med_condition),
                                             name = "House Quantity")) +
      theme_minimal()
  })
  
  # SCATTER PLOT
  output$scatter_plot <- renderPlot({
    
    # Managing the data for selected city
    if (input$select_city == "ALL (JABODETABEK)") {
      attributes_per_city <- jabodetabek_house_price
    }
    else {
      attributes_per_city <- jabodetabek_house_price %>%
        filter(city == input$select_city)
    }
    
    # Create the scatter plot
    ggplot(attributes_per_city,
           aes(x = !!sym(input$select_property_attribute),
               y = price_in_rp)) +
      geom_point(size = 1, color = "lightskyblue1") +
      geom_smooth(method = "lm", color = "lightskyblue4")+
      labs(x = "Property Attribute", y = "House Price (IDR in Billion)") +
      scale_y_continuous(labels = function(x) paste0(x/1000000000)) +
      theme_minimal()
  })
  
  # BOX PLOT
  output$box_plot <- renderPlot({
    
    # Managing the data for selected city
    if (input$select_city == "ALL (JABODETABEK)") {
      facilities_per_city <- jabodetabek_house_price
    }
    else {
      facilities_per_city <- jabodetabek_house_price %>%
        filter(city == input$select_city)
    }
    
    ggplot(facilities_per_city,
           aes(x = reorder(!!sym(input$select_facility), -price_in_rp),
               y = price_in_rp)) +
      geom_boxplot(color = "steelblue3", width = 0.5) +
      labs(x = "Facility", y = "House Price (IDR in Billion)") +
      scale_y_continuous(labels = function(x) paste0(x / 1000000000),
                         limits = c(0,10000000000)) +
      theme_minimal()
  })
  
}

# Run the shiny app

shinyApp(ui, server)

using Npgsql;

var builder = WebApplication.CreateBuilder(args);

// Basic Swagger Setup
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Swagger Middleware (Always on for now so we can test)
app.UseSwagger();
app.UseSwaggerUI();

// Database Connection String
string connectionString = "Host=mubashir-db;Database=postgres;Username=postgres;Password=mubashir.105";

app.MapGet("/", () => "Mubashir .NET 9 API is Live and Running!");

// API to get news from Database
app.MapGet("/api/banking-news", async () =>
{
    var newsList = new List<object>();
    try 
    {
        using var conn = new NpgsqlConnection(connectionString);
        await conn.OpenAsync();

        using var cmd = new NpgsqlCommand("SELECT title, source, status FROM tech_news", conn);
        using var reader = await cmd.ExecuteReaderAsync();
        
        while (await reader.ReadAsync())
        {
            newsList.Add(new { 
                Title = reader.GetString(0), 
                Source = reader.GetString(1), 
                Status = reader.GetString(2) 
            });
        }
        return Results.Ok(new { System = "Mubashir .NET 9 Portal", Data = newsList });
    }
    catch (Exception ex)
    {
        return Results.Problem($"Database Error: {ex.Message}");
    }
});

app.Run();

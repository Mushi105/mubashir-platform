FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["Mubashir.Api/Mubashir.Api.csproj", "Mubashir.Api/"]
RUN dotnet restore "Mubashir.Api/Mubashir.Api.csproj"
COPY . .
WORKDIR "/src/Mubashir.Api"
RUN dotnet build "Mubashir.Api.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Mubashir.Api.csproj" -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Mubashir.Api.dll"]

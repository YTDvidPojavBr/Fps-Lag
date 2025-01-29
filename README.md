-- Criando o GUI
local ScreenGui = Instance.new("ScreenGui")
local Frame = Instance.new("Frame")
local FPSLabel = Instance.new("TextLabel")
local PingLabel = Instance.new("TextLabel")

-- Propriedades principais do GUI
ScreenGui.Parent = game.CoreGui
ScreenGui.Name = "FPS_Ping_GUI"

Frame.Parent = ScreenGui
Frame.Size = UDim2.new(0, 200, 0, 50)
Frame.Position = UDim2.new(0.5, -100, 0.5, -25)  -- Começa no centro da tela
Frame.BackgroundColor3 = Color3.fromRGB(50, 50, 50)  -- Cor cinza
Frame.BackgroundTransparency = 0.5  -- Fundo meio transparente (ajuste a opacidade)
Frame.BorderSizePixel = 0

-- Propriedades do FPS Label
FPSLabel.Parent = Frame
FPSLabel.Size = UDim2.new(0, 100, 1, 0)
FPSLabel.Position = UDim2.new(0, 0, 0, 0)
FPSLabel.Text = "FPS: ??"
FPSLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
FPSLabel.Font = Enum.Font.GothamBold
FPSLabel.TextSize = 14
FPSLabel.TextXAlignment = Enum.TextXAlignment.Left

-- Propriedades do Ping Label
PingLabel.Parent = Frame
PingLabel.Size = UDim2.new(0, 100, 1, 0)
PingLabel.Position = UDim2.new(0.5, 0, 0, 0)
PingLabel.Text = "Ping: ?? ms"
PingLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
PingLabel.Font = Enum.Font.GothamBold
PingLabel.TextSize = 14
PingLabel.TextXAlignment = Enum.TextXAlignment.Left

-- Função para atualizar FPS
game:GetService("RunService").RenderStepped:Connect(function()
    FPSLabel.Text = "FPS: " .. math.floor(1 / game:GetService("RunService").RenderStepped:Wait()))
end)

-- Função para atualizar Ping
game:GetService("RunService").Heartbeat:Connect(function()
    local ping = game:GetService("Stats").Network.ServerStatsItem["Data Ping"]:GetValue()
    PingLabel.Text = "Ping: " .. ping .. " ms"
end)

-- Função para mover o GUI com o mouse
local dragging = false
local dragInput, dragStart, startPos

Frame.InputBegan:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.MouseButton1 then
        dragging = true
        dragStart = input.Position
        startPos = Frame.Position
    end
end)

Frame.InputChanged:Connect(function(input)
    if dragging and input.UserInputType == Enum.UserInputType.MouseMovement then
        local delta = input.Position - dragStart
        Frame.Position = UDim2.new(startPos.X.Scale, startPos.X.Offset + delta.X, startPos.Y.Scale, startPos.Y.Offset + delta.Y)
    end
end)

Frame.InputEnded:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.MouseButton1 then
        dragging = false
    end
end)

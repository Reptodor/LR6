using UnityEngine;

public class Stamina
{
    private readonly StaminaView _staminaView;
    private readonly StaminaModel _staminaModel;

    public bool CanUse => _staminaModel.CanUse();

    public Stamina(StaminaView staminaView, float baseStamina)
    {
        _staminaView = staminaView;
        _staminaModel = new StaminaModel(baseStamina);
    }

    public void Subscribe()
    {
        _staminaModel.ValueChanged += _staminaView.Display;
    }

    public void Unsubscribe()
    {
        _staminaModel.ValueChanged -= _staminaView.Display;
    }

    public void Use()
    {
        _staminaModel.Reduce(Time.deltaTime);
    }

    public void Restore()
    {
        _staminaModel.Increase(Time.deltaTime);
    }
}
